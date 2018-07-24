<template>
  <div class="hello">
    <h2>{{teamName}}</h2>
    <div v-if="!(teamName && uid)" style="width:auto;float:right;display:flex;justify-content: space-between">
      <router-link class="profile" to="/register">组队</router-link>
      <ruoter-link class="profile" to="/login">登录</ruoter-link>

    </div>


    <div v-if="(teamName && uid)" style="width:auto;float:right;display:flex;justify-content: space-between">

      <router-link class="profile" to="/sandbox">沙盒</router-link>
      <router-link class="profile" to="/submission">提交</router-link>
      <router-link class="profile" to="/record">战绩</router-link>
      <router-link class="profile" to="/key">秘钥</router-link>

    </div>

    <vuetable ref="vuetable"
              api-url="https://vuetable.ratiw.net/api/users"
              :fields="['name', 'email', 'birthdate']"
    ></vuetable>

  </div>
</template>

<script>
  import Vuetable from 'vuetable-2/src/components/Vuetable'

  export default {
  name: 'HelloWorld',
  data () {
    return {
      teamName: localStorage.getItem("name"),
      uid: localStorage.getItem("uid"),
      msg: 'Onion Datathon'
    }
  },
    components: { Vuetable }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
  .profile {
    padding: 10px;
  }
</style>
