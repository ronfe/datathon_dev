<template>

  <vuetable ref="vuetable"
            api-url="http://localhost:5000/teamLogs/真诚的苍鹰"
            :fields="['status', 'uploadTime']"
  ></vuetable>
</template>

<script>
  const web = require('../web');
  import Vuetable from 'vuetable-2/src/components/Vuetable'

  export default {
    data: function(){
      return {
        teamName: localStorage.getItem("name"),
        apiURL: web.baseURL + '/teamLogs' + localStorage.getItem("name")
      }
    },
    components: { Vuetable }
  }

</script>
