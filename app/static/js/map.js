// Interactive globe for the team's "interesting places".
//
// Reads the place data embedded in #places-data, draws a dark themed globe with
// one coloured point per city and an arc "journey" per teammate, then wires the
// side-panel buttons so a city flies the camera there and a name plays a tour.
//
// globe.gl docs: https://github.com/vasturiano/globe.gl

document.addEventListener("DOMContentLoaded", () => {
    const stage = document.getElementById("globe");
    const dataEl = document.getElementById("places-data");
    const caption = document.getElementById("globe-caption");

    // If the CDN failed or the elements are missing, leave the panel working on its own.
    if (!stage || !dataEl || typeof Globe === "undefined") {
        if (caption) {
            caption.textContent = "Globe couldn't load — the place list still works.";
        }
        return;
    }

    const team = JSON.parse(dataEl.textContent);

    // Flatten to points, tagging each with its owner's colour and name.
    const points = team.flatMap((person) =>
        person.places.map((place) => ({
            ...place,
            member: person.member,
            color: person.color,
        }))
    );

    // One arc per consecutive pair of a person's cities = their travel "thread".
    const arcs = team.flatMap((person) =>
        person.places.slice(1).map((place, index) => {
            const from = person.places[index];
            return {
                startLat: from.lat,
                startLng: from.lng,
                endLat: place.lat,
                endLng: place.lng,
                color: person.color,
            };
        })
    );

    const globe = Globe()(stage)
        .globeImageUrl("//unpkg.com/three-globe/example/img/earth-dark.jpg")
        .bumpImageUrl("//unpkg.com/three-globe/example/img/earth-topology.png")
        .backgroundImageUrl("//unpkg.com/three-globe/example/img/night-sky.png")
        .atmosphereColor("#6ea8ff")
        .atmosphereAltitude(0.18)
        // Points
        .pointsData(points)
        .pointLat("lat")
        .pointLng("lng")
        .pointColor("color")
        .pointAltitude(0.02)
        .pointRadius(0.42)
        .pointLabel((d) => `<div class="globe-point-label">
                <strong>${d.name}</strong><br>${d.tag}<br>
                <span style="color:${d.color}">${d.member}</span>
            </div>`)
        .onPointClick((d) => flyTo(d))
        // Glowing rings so the cities feel alive rather than like flat pins.
        .ringsData(points)
        .ringLat("lat")
        .ringLng("lng")
        .ringColor((d) => () => d.color)
        .ringMaxRadius(2.2)
        .ringPropagationSpeed(1.4)
        .ringRepeatPeriod(1400)
        // Arcs
        .arcsData(arcs)
        .arcColor("color")
        .arcStroke(0.4)
        .arcAltitudeAutoScale(0.4)
        .arcDashLength(0.5)
        .arcDashGap(0.25)
        .arcDashAnimateTime(2600);

    // Gentle idle spin; pauses while the user is dragging.
    const controls = globe.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.5;
    controls.enableZoom = true;
    controls.addEventListener("start", () => { controls.autoRotate = false; });

    // Start the camera looking at North America where most of the team is based.
    globe.pointOfView({ lat: 30, lng: -90, altitude: 2.4 }, 0);

    // --- Sizing: globe.gl needs explicit pixel dimensions ---
    const sizeGlobe = () => {
        const rect = stage.getBoundingClientRect();
        globe.width(rect.width).height(rect.height);
    };
    sizeGlobe();
    window.addEventListener("resize", sizeGlobe);

    // --- Fly the camera to a place and show its caption ---
    let tourTimers = [];
    const clearTour = () => {
        tourTimers.forEach((t) => window.clearTimeout(t));
        tourTimers = [];
    };

    const showCaption = (place) => {
        if (!caption) return;
        caption.innerHTML =
            `<strong>${place.name}</strong> — ${place.tag}` +
            (place.member ? ` <span class="globe-caption-member">(${place.member})</span>` : "");
        caption.classList.add("is-visible");
    };

    const flyTo = (place, altitude = 1.6) => {
        controls.autoRotate = false;
        globe.pointOfView({ lat: place.lat, lng: place.lng, altitude }, 1200);
        showCaption(place);
    };

    // --- Wire the side panel ---
    document.querySelectorAll(".globe-place-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            clearTour();
            flyTo({
                name: btn.dataset.name,
                tag: btn.dataset.tag,
                lat: parseFloat(btn.dataset.lat),
                lng: parseFloat(btn.dataset.lng),
            });
            highlight(btn);
        });
    });

    document.querySelectorAll(".globe-member-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
            clearTour();
            const person = team.find((p) => p.member === btn.dataset.member);
            if (person) playTour(person);
        });
    });

    // Visually mark the active city chip.
    const highlight = (btn) => {
        document.querySelectorAll(".globe-place-btn.is-active")
            .forEach((b) => b.classList.remove("is-active"));
        if (btn) btn.classList.add("is-active");
    };

    // Step through one person's cities, ~2.6s apart, captioning each stop.
    const playTour = (person) => {
        person.places.forEach((place, index) => {
            const timer = window.setTimeout(() => {
                flyTo({ ...place, member: person.member }, 1.5);
                const chip = document.querySelector(
                    `.globe-place-btn[data-name="${CSS.escape(place.name)}"]`
                );
                highlight(chip);
            }, index * 2600);
            tourTimers.push(timer);
        });
    };
});
