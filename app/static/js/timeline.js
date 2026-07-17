/**
 * Fetch JSON only when it conforms to the shape expected by the caller.
 *
 * @param {string} url
 * @param {(data: unknown) => data is T} isT
 * @returns {Promise<T>}
 */
function typedFetch(url, isT) {
    return fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(response.statusText || `Request failed with ${response.status}`);
            }

            return response.json();
        })
        .then((data) => {
            if (!isT(data)) {
                throw new Error("Invalid response");
            }

            return data;
        });
}

const AMAR_COLOR = "#ff6b6b";

/** 
 * @param {unknown} value 
 * @returns {value is string} */
function isString(value) {
    return typeof value === "string";
}

/** 
 * @param {unknown} data 
 * */
function isTimelinePostsResponse(data) {
    return typeof data === "object" && data !== null
        && "timeline_posts" in data
        && Array.isArray(data.timeline_posts)
        && data.timeline_posts.every((post) => (
            typeof post === "object" && post !== null
            && "name" in post && isString(post.name)
            && "email" in post && isString(post.email)
            && "content" in post && isString(post.content)
        ));
}

/**
 * @param {{ name: string, email: string, content: string }} post
 * @returns {HTMLLIElement}
 */
function createTimelineItem(post) {
    const item = document.createElement("li");
    item.className = "work-item";

    const marker = document.createElement("div");
    marker.className = "work-marker";

    const card = document.createElement("div");
    card.className = "work-card";

    const name = document.createElement("h3");
    name.className = "work-title";
    name.textContent = post.name;

    const email = document.createElement("p");
    email.className = "work-org";
    email.textContent = post.email;

    const description = document.createElement("p");
    description.className = "work-summary";
    description.textContent = post.content;

    card.append(name, email, description);
    item.append(marker, card);
    return item;
}

document.addEventListener("DOMContentLoaded", async () => {
    const timelineBoard = document.querySelector("#timeline-board");
    const form = document.querySelector("#form")

    if (!(timelineBoard instanceof HTMLElement)) {
        return;
    }

    try {
        const { timeline_posts: posts } = await typedFetch(
            "/api/timeline_post",
            isTimelinePostsResponse,
        );

        const column = document.createElement("section");
        column.className = "work-column";
        column.style.setProperty("--member-color", AMAR_COLOR);

        const timeline = document.createElement("ol");
        timeline.className = "work-timeline";
        posts.forEach((post) => {timeline.appendChild(createTimelineItem(post))});

        column.appendChild(timeline);
        timelineBoard.replaceChildren(column);
    } catch (error) {
        const errorElement = document.createElement("p");
        errorElement.className = "timeline-error";
        errorElement.setAttribute("role", "alert");
        errorElement.textContent = error instanceof Error
            ? `Unable to load timeline posts: ${error.message}`
            : "Unable to load timeline posts.";
        timelineBoard.replaceChildren(errorElement);
    }

    form.removeAttribute("hidden");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        e.stopPropagation();

        // prevent submit button from being hit again
        form.querySelector("#form-submit").style.display = "none"; 


        // Safely cast currentTarget to HTMLFormElement
        const formElement = e.currentTarget;
        
        // Extract data using FormData
        const formData = new FormData(formElement);
        
        // Convert payload to a structured key-value object
        const payload = Object.fromEntries(formData.entries());

        const timeline = document.querySelector("work-timeline");
        
        if (timeline instanceof HTMLElement){
            timeline.appendChild(createTimelineItem(payload));
        }

        // readd submit button 
        form.querySelector("#form-submit").style.display = "block"; 

    });

});
