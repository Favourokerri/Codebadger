let profilePic = document.getElementById('profile-picture');
let inputImage = document.getElementById('input-image');
let removeImage = document.getElementById('remove-image');
const defaultImageSrc = profilePic.getAttribute('data-default-src');



//code to display selected student image
inputImage.onchange = function(){
    profilePic.src = URL.createObjectURL(inputImage.files[0]);
    console.log(inputImage.files);
}

removeImage.onclick = function(){
    profilePic.src = defaultImageSrc;
}