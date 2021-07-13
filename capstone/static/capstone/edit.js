document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#link_edit').onclick = () => {
        document.querySelector('#edit').style.display = 'block';
        const x = document.querySelector('#edit');
        x.children[0].children[0].value = x.children[0].children[0].dataset.name;
        x.children[3].children[0].value = x.children[3].children[0].dataset.description;
        x.children[4].children[0].value = x.children[4].children[0].dataset.venue;
    }
    document.querySelector('#edit').children[5].children[0].onclick = () => {
        const x = document.querySelector('#edit');
        fetch(`/edit/${document.querySelector('#edit').dataset.id}`, {
            method:'PUT',
            body:JSON.stringify({
                name:x.children[0].children[0].value,
                date:x.children[1].children[0].value,
                start_time:x.children[2].children[0].value,
                end_time:x.children[2].children[1].value,
                description:x.children[3].children[0].value,
                venue:x.children[4].children[0].value
            })
        })
        document.querySelector('#edit').style.display = 'none';
        document.querySelector('#part_available_to_edit').innerHTML = `<div>About the event: ${x.children[3].children[0].value}</div><div>To be held on: ${x.children[1].children[0].value}. Venue: ${x.children[4].children[0].value}</div><div>From: ${x.children[2].children[0].value} To: ${x.children[2].children[1].value}</div>`;
    }
})