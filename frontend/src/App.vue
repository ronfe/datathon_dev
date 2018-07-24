<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <h1>{{ msg }}</h1>

    <router-view />

  </div>
</template>

<script>
export default
{
  name: 'PointingMenuSecondaryExample',
    data() {
      let x = {
        teamName: localStorage.getItem("name"),
        uid: localStorage.getItem("uid"),
        msg: 'Onion Datathon'
      };
  return x;
},
  methods: {
    isActive(name) {
      return this.active === name;
    },
    select(name) {
      this.active = name;
    },
  },
};

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px;
}
  .profile {
    padding-top: 1em;
    text-align:center;
    font-size: 20px;
  }
</style>
