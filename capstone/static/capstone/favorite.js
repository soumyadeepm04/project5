document.addEventListener('DOMContentLoaded', () => {
    window.onload = PageLoad();
    const checkbox = document.querySelector('#favorite_checkbox')
    document.querySelector('#favorite_checkbox').onchange = () => {
        if (checkbox.checked){
            fetch(`/favorite/${checkbox.dataset.id}`, {
                method:'POST'
            })
        }
        else{
            fetch(`/unfavorite/${checkbox.dataset.id}`, {
                method:'PUT'
            })
        }
    }
})

function PageLoad(){
    if (document.querySelector('#favorite_checkbox').dataset.exists == 'True'){
        document.querySelector('#favorite_checkbox').checked = true;
    }
}