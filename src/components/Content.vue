<template>
  <div class="hello">
    <ul>
      <li>
        <img v-bind:src="imgUrl" width="220" height="220" />
      </li>
      <li>
        <SpeciesStrengthRadar v-bind::ss="ss" />
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
  },
  components: {
    SpeciesStrengthRadar,
  },
  data() {
    const { data } = require("../assets/data/" + this.bid + ".js");
    return {
      articleDetail: data.content,
      imgUrl: data.url,
      ss: data.ss,
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
  margin-block-start: 0;
}
li {
  display: inline;
}
</style>
