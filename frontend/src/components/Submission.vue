<template>
    <vue-dropzone ref="myVueDropzone"
                  id="dropzone"
                  :options="dropzoneOptions"
                  v-on:vdropzone-sending="sendingEvent"></vue-dropzone>

</template>

<script>
  import vue2Dropzone from 'vue2-dropzone'
  import 'vue2-dropzone/dist/vue2Dropzone.min.css'
  export default {
    components: {
      vueDropzone: vue2Dropzone
    },
    data: function(){

      return {
        dropzoneOptions: {
          url: 'http://localhost:5000/upload',
          thumbnailWidth: 150,
//          maxFilesize: 0.5,
          headers: { "My-Awesome-Header": "header value" }

        }
      }
    },

    methods: {
      sendingEvent (file, xhr, formData){
        let teamName = localStorage.getItem('name');
        console.log(teamName);
        formData.append('teamName', teamName);
      }
    }
  }
</script>

<style>
  @import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");

</style>
