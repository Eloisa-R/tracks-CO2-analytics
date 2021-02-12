import Vue from 'vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faBus, faArrowsAltV } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import router from './router';
import App from './App.vue';
import filters from './filters';

library.add(faBus);
library.add(faArrowsAltV);

Vue.use(filters);

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
