document.addEventListener('DOMContentLoaded', () => {
    window.onload = OnPageLoad();
    const checkbox = document.querySelector('#register_checkbox')
    let num_registered = checkbox.dataset.num_registered
    checkbox.onchange = () => {
        if (checkbox.checked){
            fetch(`/register_event/${checkbox.dataset.id}`, {
                method: 'POST'
            })
            num_registered++;
            document.querySelector('#registered').innerHTML = `Number of people registered for the event: ${num_registered}`
        }
        else{
            fetch(`/unregister_event/${checkbox.dataset.id}`, {
                method:'POST'
            })
            num_registered--;
            document.querySelector('#registered').innerHTML = `Number of people registered for the event: ${num_registered}`
        }
    }
})

function OnPageLoad(){
    if (document.querySelector('#register_checkbox').dataset.exists == 'True'){
        document.querySelector('#register_checkbox').checked = true;
    }
}