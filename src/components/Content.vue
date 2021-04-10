<template>
  <div class="hello">
    <ul>
      <li>
        <el-carousel
          :autoplay="false"
          indicator-position="outside"
          :height="dataHeight"
        >
          <el-carousel-item  v-for="item in imgUrls.length" :key="item">
            <img v-bind:src="imgUrls[item-1]" width="220" height="220" />
          </el-carousel-item>
        </el-carousel>
      </li>
      <li>
        <SpeciesStrengthRadar v-bind:ss="ss" />
      </li>
    </ul>
    <article class="context" v-html="compiledMarkdown"></article>
  </div>
</template>

<script>
import SpeciesStrengthRadar from "./SpeciesStrengthRadar.vue";
import marked from "marked";

export default {
  name: "Content",
  props: {
    bid: String,
    label: String,
  },
  components: {
    SpeciesStrengthRadar,
  },
  data() {
    const { data } = require("../assets/data/" + this.bid + ".js");
    return {
      articleDetail: data.content,
      imgUrls: data.urls,
      ss: data.ss,
      dataHeight: "220px",
    };
  },
  computed: {
    compiledMarkdown() {
      return marked(this.articleDetail);
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
p {
  word-wrap: break-word;
  word-break: normal;
}

ul {
  align-content: center;
  float: right;
  width: 250px;
  margin-block-start: 0;
}
li {
  display: inline;
}

.el-carousel {
    width: 220px;
    margin: 0 auto;
}


</style>
