document.addEventListener('DOMContentLoaded', function() {
    escrevendoLetra();
    ativacaoMenu();
    sobreMim();
});

function escrevendoLetra() {
    function ativaLetra(elemento) {
        const arrTexto = elemento.innerHTML.split('');
        elemento.innerHTML = '';
        arrTexto.forEach((letra, i) => {
            setTimeout(() => {
                elemento.innerHTML += letra;
            }, 75 * i);
        });
    }

    const titulo = document.querySelector('.digitando');
    if (titulo) ativaLetra(titulo);
}

function ativacaoMenu() {
    const ativaMenu = document.querySelector('.fa-bars');
    const navMenu = document.querySelector('header .navegacao-primaria');

    if (ativaMenu && navMenu) {
        ativaMenu.addEventListener('click', () => {
            ativaMenu.classList.toggle('fa-x');
            navMenu.classList.toggle('ativado');
        });
    }
}

function sobreMim() {
    const experiencia = document.querySelectorAll('.experience_content div');
    const botao = document.querySelectorAll('.experience_content ul li');
    const education = document.querySelectorAll('.education_content div');
    const botaoEducation = document.querySelectorAll('.education_content ul li');

    if (experiencia.length > 0 && botao.length > 0) {
        experiencia[0].classList.add('ativo');
        botao[0].classList.add('ativo');
    }
    if (education.length > 0 && botaoEducation.length > 0) {
        education[0].classList.add('ativo');
        botaoEducation[0].classList.add('ativo');
    }

    function slideShow(index) {
        experiencia.forEach((divisao) => {
            divisao.classList.remove('ativo');
        });
        botao.forEach((item) => {
            item.classList.remove('ativo');
        });
        experiencia[index].classList.add('ativo');
        botao[index].classList.add('ativo');
    }

    function slideShow2(index) {
        education.forEach((divisao) => {
            divisao.classList.remove('ativo');
        });
        botaoEducation.forEach((item) => {
            item.classList.remove('ativo');
        });
        education[index].classList.add('ativo');
        botaoEducation[index].classList.add('ativo');
    }

    botao.forEach((event, index) => {
        event.addEventListener('click', () => {
            slideShow(index);
        });
    });

    botaoEducation.forEach((div, index) => {
        div.addEventListener('click', () => {
            slideShow2(index);
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const listaALL = document.querySelectorAll('.projects_armazenamento ul li');
    const buttonGeral = document.querySelectorAll('.project_navegacao li');

    function removeClick(index) {
        buttonGeral.forEach((item) => {
            item.classList.remove('ativo');
        });
        buttonGeral[index].classList.add('ativo');
    }

    function showLista(lista, buttom = "all") {
        lista.forEach((item) => {
            item.classList.remove('ativo');
        });

        if (buttom == 'website') {
            lista.forEach((item) => {
                if (item.classList.contains('website')) {
                    item.classList.add('ativo');
                }
            });
        }

        if (buttom == 'design') {
            lista.forEach((item) => {
                if (item.classList.contains('design')) {
                    item.classList.add('ativo');
                }
            });
        }

        if (buttom == 'sistema') {
            lista.forEach((item) => {
                if (item.classList.contains('sistema')) {
                    item.classList.add('ativo');
                }
            });
        }

        if (buttom == 'all') {
            lista.forEach((item) => item.classList.add('ativo'));
        }
    }

    buttonGeral.forEach((item, index) => {
        item.addEventListener('click', (e) => {
            let currentButton = e.target;
            if (currentButton.classList.contains('all')) {
                showLista(listaALL, 'all');
            } 
            if (currentButton.classList.contains('website')) {
                showLista(listaALL, 'website');
            }
            if (currentButton.classList.contains('design')) {
                showLista(listaALL, 'design');
            }
            if (currentButton.classList.contains('sistema')) {
                showLista(listaALL, 'sistema');
            }
            removeClick(index);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const scrollToTopButton = document.querySelector('.scroll-to-top');

    if (scrollToTopButton) {  
        window.addEventListener('scroll', function() {
            if (window.scrollY > 200) {
                scrollToTopButton.style.display = 'block';
            } else {
                scrollToTopButton.style.display = 'none';
            }
        });

        scrollToTopButton.addEventListener('click', function(event) {
            event.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    } else {
        console.warn("Botão de rolar para o topo não encontrado na página.");
    }
});
