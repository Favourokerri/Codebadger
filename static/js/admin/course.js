document.addEventListener('DOMContentLoaded', function(){
    const publishedLink = document.getElementById('publishedLink');
    const draftLink = document.getElementById('draftLink');

    function handelStatusClick(event){
        publishedLink.classList.remove('status-active');
        draftLink.classList.remove('status-active');
    }

    const currentLocation = window.location.href;
    if (currentLocation.includes('publishedCourse')){
        publishedLink.classList.add('status-active')
    } 

    else if (currentLocation.includes('draftCourse')){
        draftLink.classList.add('status-active')
    }

    publishedLink.addEventListener('click', handelStatusClick);
    draftLink.addEventListener('click', handelStatusClick);

})