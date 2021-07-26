document.addEventListener("DOMContentLoaded", function(event){
    console.log("Hello It is working")
    let sc = document.createElement('script')
    sc.setAttribute('src', 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js')

    document.head.append(sc);
    sc.onload = ()=>{
        tinymce.init({
            selector: '#id_content'
          });
    }


})