<template>
  <div id="app">
    <el-row>
      <el-col :span="5">
        <div class="search">
          <el-input placeholder="输入关键字进行过滤" v-model="filterText">
          </el-input>

          <el-tree
            class="filter-tree"
            :data="data"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            ref="tree"
          >
          </el-tree>
        </div>
      </el-col>
      <el-col :span="19">
        <Content :bid="bid" v-if="selected" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Content from "./components/Content.vue";
import { indexes } from "./assets/data/indexes.js";

export default {
  name: "App",
  data() {
    return {
      bid: "001",
      selected: true,
      //
      filterText: "",
      data: indexes,
      defaultProps: {
        children: "children",
        label: "label",
      },
    };
  },
  components: {
    Content,
  },
  methods: {
    filterNode(value, data) {
      if (!value) return true;
      if (data.label.indexOf(value) === -1) return false;

      if (data.bid === undefined) return true;
      if (this.bid !== "") return true;

      this.selected = false;
      this.bid = data.bid; // TODO
      this.$nextTick(() => {
        console.log("rendering ", this.bid);
        this.selected = true;
      });

      return true;
    },
  },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
      if (this.selected === true) this.bid = "";
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 10px;
  margin-left: 10px;
}
.search {
  margin-right: 30px;
}
.filter-tree {
  margin-top: 20px;
}
</style>
