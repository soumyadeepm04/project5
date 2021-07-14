document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.approve').forEach(element => {
        element.onclick = () => {
            fetch(`/approve_restoration/${element.dataset.id}`, {
                method:'PUT'
            })
            document.getElementById(`${element.dataset.id}`).style.display = 'none';
        }
    })
    document.querySelectorAll('.reject').forEach(element => {
        element.onclick = () => {
            fetch(`/reject_restoration/${element.dataset.id}`, {
                method:'PUT'
            })
            document.getElementById(`${element.dataset.id}`).style.display = 'none';
        }
    })
})