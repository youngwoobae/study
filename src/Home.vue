<template>
  <div id="app">
    <div>
      <v-row>
        <v-row style="display:flex; justify-content:center; margin: 50px">
          <v-col>
            <router-link to="/Tourism"><img alt="Vue logo" src="./assets/관광.png" class="mainPhoto"><p>국내 여행</p></router-link>
          </v-col>
          <!-- <v-col>
            <router-link to="/Hiking"><img alt="Vue logo" src="./assets/하이킹.png" class="mainPhoto"><p>하이킹</p></router-link>
          </v-col>
          <v-col>
            <router-link to="/Jeju"><img alt="Vue logo" src="./assets/제주도.png" class="mainPhoto"><p>제주</p></router-link>
          </v-col> -->
          <v-col style="margin-left: 150px;">
            <router-link to="/overseasTrip"><img alt="Vue logo" src="./assets/해외.png" class="mainPhoto"><p>해외 여행</p></router-link>
          </v-col>
        </v-row>
      </v-row>
      <v-row style="align-items: ;">
        <span>hiiiiiii</span>
      </v-row>
    </div>
  </div>
</template> 

<script>

export default {
  name: 'Home',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: grid;
  place-items: center;
  min-height: 70vh;
}

.mainPhoto{
  width: 250px;
  float: left;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
