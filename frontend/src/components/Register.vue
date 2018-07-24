<template>
  <div>
    <h1>组建战队</h1>


    <div>
      <div style="width:15em;margin:auto; padding-bottom: 10px;">
        <label>团队名称: <span style="font-size:20pt;color:blue;">{{teamName}} </span>(团队名称自动生成)</label>
        <!--<input v-model="teamName" placeholder="X 战队" >-->
      </div>
      <div style="margin:auto;">
        <label>包含成员:</label>
        <sui-checkbox style="margin:auto;display:block;width:10em;padding:3px;"
                      v-for="each in candidates"
                      :label="each"
                      :value="each"
                      v-model="selectedCandidates"
        />
      </div>

    </div>
    <button
      :disabled="selectedCandidates.length <= 0 || selectedCandidates.length > 3"
      v-on:click="submitForm()">Submit</button>


    <div>注意:每人只能参加一个战队,每战队最多三人</div>

    <div>
      <sui-modal v-model="open">
        <sui-modal-header>创建成功!</sui-modal-header>
        <sui-modal-content image>
          <sui-modal-description>
            <sui-header>团队名称:{{teamName}}</sui-header>
            <p>秘钥: {{uid}} </p>
            <p>在非本地登录需要提供秘钥</p>
            <p>团队成员:</p>
            <p v-for="member in selectedCandidates">{{member}}</p>
          </sui-modal-description>
        </sui-modal-content>
        <sui-modal-actions>
          <sui-button floated="right" positive @click.native="open=false;">
            OK
          </sui-button>
        </sui-modal-actions>
      </sui-modal>
    </div>


  </div>
</template>

<script>
  const web = require('../web');
  export default {
    name: 'Register',
    data() {

      let x = {
        teamName: "",
        candidates: [],
        selectedCandidates: [],
        naCandidates: [],
        uid: "",
        open: false
      }

      web.get('/users').then(function(res){
        x.candidates = res.data.candidates;
        x.naCandidates = res.data.naCandidates;
      });

      x.teamName = localStorage.getItem("name");
      if (!x.teamName) {
        web.get('/teamName').then(function(res){
          x.teamName = res.data.name;
          localStorage.setItem("name", x.teamName);
        });
      }

      return x},
    methods: {
      submitForm() {
        const vm = this;
        if (!localStorage.getItem('uid')){
          web.post('/joinTeam', {
            users: this.selectedCandidates,
            teamName: this.teamName
          }).then(function(res){
            vm.uid = res.data.uid;
            localStorage.setItem("uid", vm.uid);
            vm.open = true;
          })
        }

      },
      select(name) {
        this.active = name;
      },
    }
  };
</script>
