
document.addEventListener("DOMContentLoaded", function () {
    const loadingIndicator = document.getElementById('loader');
    const vacanciesContainer = document.getElementById('vacancies');
    const footerContainer = document.getElementById('footer');
    footerContainer.style.display = 'none'
    loadingIndicator.style.display = 'block';

    

    fetch('/api/last_vac/')
        .then(response => response.json())
        .then(data => {
            loadingIndicator.style.display = 'none'; 
            
            if (data.length > 0) {
                data.forEach(vacancy => {
                    const vacancyDiv = document.createElement('div');
                    vacancyDiv.className = 'vacancy';
                    
                    const descriptionDiv = document.createElement('div');
                    descriptionDiv.className = 'vac-description';
                    descriptionDiv.innerHTML = vacancy.description;
                    descriptionDiv.style.display = 'none';

                    const toggleButton = document.createElement('button');
                    toggleButton.className = 'show-description';
                    toggleButton.innerText = 'Показать описание';
                    toggleButton.onclick = function () {
                        
                        if (descriptionDiv.style.display === 'none') {
                            descriptionDiv.style.display = 'block';
                            toggleButton.innerText = 'Скрыть описание';
                        } else {
                            descriptionDiv.style.display = 'none';
                            toggleButton.innerText = 'Показать описание';
                        
                        };
                    }

                    vacancyDiv.innerHTML =
                        `<div class='vac-title'>${vacancy.title}</div>
                        <div class="vac-elem">${vacancy.skills}</div>
                        <div class="vac-elem">${vacancy.company}</div>
                        <div class="vac-salary vac-elem">${vacancy.salary}</div>
                        <div class="vac-elem">${vacancy.region}</div>
                        <div class="vac-published_at vac-elem">${vacancy.published_at}</div>`;
                    vacanciesContainer.appendChild(vacancyDiv);
                    vacancyDiv.appendChild(descriptionDiv);
                    vacancyDiv.appendChild(toggleButton);
                    vacanciesContainer.appendChild(vacancyDiv);
                });
            } else {
                vacanciesContainer.innerHTML = '<p>Нет доступных вакансий</p>';
            }
            footerContainer.style.display = 'block'
        })
        .catch(error => {
            loadingIndicator.style.display = 'none'; 
            vacanciesContainer.innerHTML = '<p>Ошибка загрузки вакансий</p>';
            console.error('Ошибка:', error);
        });
});