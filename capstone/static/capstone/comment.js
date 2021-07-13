document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#comment').onclick = () => {
        document.querySelector('#type_comment').style.display = 'block';
    }
    const x = document.querySelector('#type_comment')
    x.children[1].children[0].onclick = () => {
        console.log(x.dataset.owner);
        fetch('/comment', {
            method: 'POST',
            body:JSON.stringify({
                comment: x.children[0].children[0].value,
                event_id: x.dataset.id,
                event_owner:x.dataset.owner
            })
        })
        x.children[0].children[0].value = ''
        x.style.display = 'none';
        alert('Your comment will be displayed after it is authorized by the user who created this event!');
    }
})