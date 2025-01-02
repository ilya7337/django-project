let selectYearEl;
let url;

if (document.querySelector('.select-year')) {
    selectYearEl = document.querySelector('.select-year');
    url = `/api/top_skills/profession/`;
    downloadDataSkills(url, selectYearEl)
}
else if (document.querySelector('.general-select-year')) {
    selectYearEl = document.querySelector('.general-select-year');
    url = `/api/top_skills/general/`;
    downloadDataSkills(url, selectYearEl)
}

function downloadDataSkills(url, selectYearEl) {
    const year = selectYearEl.value;
    url = url.concat(year) + "/";
    console.log(url);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            contEl = document.querySelector('.top-skills-container');
            contEl.innerHTML = "";
            newImg = document.createElement('img');
            newImg.src = "/static/images/" + data[0]['image'];
            contEl.appendChild(newImg);
        })
}

if (selectYearEl) {
    selectYearEl.addEventListener("change", () => downloadDataSkills(url, selectYearEl));
}