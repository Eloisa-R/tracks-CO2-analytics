import roundUp from './decimals';

export default {
  install(Vue) {
    Vue.filter('roundUp', roundUp);
  },
};
