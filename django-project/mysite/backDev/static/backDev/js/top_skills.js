let selectYearEl;
let url;

if (document.querySelector('[name="select-year"]')) {
    selectYearEl = document.querySelector('[name="select-year"]');
    url = `/api/top_skills/profession/`;
    downloadDataSkills(url, selectYearEl)
}
else if (document.querySelector('[name="general-select-year"]')) {
    selectYearEl = document.querySelector('[name="general-select-year"]');
    url = `/api/top_skills/general/`;
    downloadDataSkills(url, selectYearEl)
}

function downloadDataSkills(url, selectYearEl) {
    const year = selectYearEl.value;
    url = url.concat(year) + "/";   
    fetch(url)
        .then(response => response.json())
        .then(data => {
            contEl = document.querySelector('.top-skills-container');
            contEl.innerHTML = "";
            newImg = document.createElement('img');
            newImg.className = 'skills-img'
            newImg.src = "/static/images/" + data[0]['image'];
            tableBlock = document.createElement('div');
            imgBlock = document.createElement('div');
            imgBlock.appendChild(newImg);
            tableBlock.className = "table-block";
            tableBlock.innerHTML = data[0]['table']
            contEl.appendChild(imgBlock);
            contEl.appendChild(tableBlock);
        })
}

if (selectYearEl) {
    selectYearEl.addEventListener("change", () => downloadDataSkills(url, selectYearEl));
}