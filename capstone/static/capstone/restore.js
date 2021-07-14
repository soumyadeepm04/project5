document.addEventListener('DOMContentLoaded', () => {
    window.onload = Load();
    document.querySelectorAll('.checkbox').forEach(element => {
        element.onchange = () => {
            if (element.checked){
                fetch(`/restore_approval/${element.dataset.id}`, {
                    method: 'POST'
                })
            }
            else{
                fetch(`/remove_approval/${element.dataset.id}`, {
                    method: 'PUT'
                })
            }
        }
    })
})
function Load(){
    document.querySelectorAll('.checkbox').forEach(element => {
        if (element.dataset.exists === 'true'){
            element.checked = true;
        }
    })
}