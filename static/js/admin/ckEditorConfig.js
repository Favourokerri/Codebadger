const {
    ClassicEditor,
    Essentials,
    Bold,
    Italic,
    Font,
    Paragraph,
    codeBlock,
} = CKEDITOR;

ClassicEditor
    .create( document.querySelector( '#editor' ), {
        plugins: [Essentials, Bold, Italic, Font, Paragraph],
        toolbar: [
            'undo', 'redo', '|', 'bold', 'italic', '|', 'codeBlock',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor'
        ]
    } )
    .then( /* ... */ )
    .catch( /* ... */ );