// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import SuiVue from "semantic-ui-vue";
import VueResource from 'vue-resource';
Vue.use(VueResource);
import 'semantic-ui-css/semantic.min.css';
import axios from 'axios'
import VueLocalStorage from 'vue-localstorage';
import vue2FileUpload from 'vue2-file-upload';
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

Vue.use(axios);
Vue.use(VueLocalStorage);
Vue.use(vue2Dropzone);

Vue.config.productionTip = false;
Vue.use(SuiVue);


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});

export const axiosConfig = {
  baseURL: "http://localhost:5000"
};
