<template>
  <div id="app">
    <nav class="navbar" role="navigation" aria-label="main navigation">
       <div class="navbar-brand">
         <div class="navbar-item">
             <span class="icon">
                <font-awesome-icon icon="bus" class="icon-color"/>
             </span>
         </div>
       </div>
    <div class="navbar-menu">
     <router-link class="navbar-item" to="/">Home</router-link>
     <router-link class="navbar-item" to="/analytics">Carriers CO2 Analytics</router-link>
    </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
@import '../node_modules/bulma/css/bulma.css';
</style>

<style scoped>
.icon-color {
  color: hsl(171, 100%, 41%);
}
</style>
