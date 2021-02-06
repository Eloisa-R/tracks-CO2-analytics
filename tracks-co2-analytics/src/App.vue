<template>
  <div id="app">
    <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-start">
     <router-link class="navbar-item" to="/">Home</router-link> |
     <router-link class="navbar-item" to="/analytics">CO2 Analytics</router-link>
    </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
