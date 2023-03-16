function showUrls() {
    let element = document.getElementById('show-btn');
    let ul = document.getElementById('list-urls');
    let hidden = ul.getAttribute('hidden');

    if (hidden) {
        ul.removeAttribute('hidden');
        element.innerText = 'Hide URLs';
    } else {
        ul.setAttribute('hidden', 'hidden');
        element.innerText = 'Show URLs';
    }

}
