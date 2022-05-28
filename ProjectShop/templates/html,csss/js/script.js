document.addEventListener('DOMContentLoaded', function () {
    const nav = document.querySelector('.navbar')

    function addShadow() {
        if (window.scrollY >= 200) {
            nav.classList.add('shadow')
        } else {
            nav.classList.remove('shadow')
        }
    }

    window.addEventListener('scroll', addShadow)
})