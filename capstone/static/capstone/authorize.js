document.addEventListener('DOMContentLoaded', () => {
    document.addEventListener('click', event => {
        document.querySelectorAll('.authorize').forEach(element => {
            if (event.target === element){
                fetch('/authorize', {
                    method:'PUT',
                    body:JSON.stringify({
                        comment:element.dataset.comment,
                        event_id:element.dataset.event_id
                    })
                })
                document.getElementById(`${element.dataset.event_id}`).style.display = 'none';
            }
        })
        document.querySelectorAll('.reject').forEach(element => {
            if (event.target === element){
                fetch('/reject', {
                    method:'PUT',
                    body:JSON.stringify({
                        comment:element.dataset.comment,
                        event_id:element.dataset.event_id
                    })
                })
                document.getElementById(`${element.dataset.event_id}`).style.display = 'none';
            }
        })
    })
})