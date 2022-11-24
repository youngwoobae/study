<template>
  <div class="header" >
    <div>
      <v-row>
        <v-col cols="3">
          <h2>Trip To Get</h2>
        </v-col>
        <v-col cols="9"></v-col>
      </v-row>
    </div>
    <router-link to="/bar">여행 일지</router-link> / <router-link to="/">메인페이지</router-link> / <router-link to="/login">여행지 추가</router-link>
  </div>

</template>

<script>
export default {
}
</script>

<style scoped>
.header {
  text-align: center;
}

a {
  color: #42b983;
} 
</style>
