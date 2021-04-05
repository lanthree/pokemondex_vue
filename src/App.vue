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

export default {
  name: "App",
  data() {
    return {
      bid: "001",
      selected: true,
      //
      filterText: "",
      data: [
        {
          id: 1,
          label: "关都图鉴",
          children: [
            {
              id: 9,
              label: "三级 1-1-1",
              bid: "001",
              match: "",
            },
            {
              id: 10,
              label: "三级 1-1-2",
              bid: "002",
            },
          ],
        },
        {
          id: 2,
          label: "成都图鉴",
          children: [
            {
              id: 5,
              label: "二级 2-1",
              bid: "003",
            },
            {
              id: 6,
              label: "二级 2-2",
              bid: "004",
            },
          ],
        },
        {
          id: 3,
          label: "丰缘图鉴",
          children: [
            {
              id: 7,
              label: "二级 3-1",
              bid: "005",
            },
            {
              id: 8,
              label: "二级 3-2",
              bid: "006",
            },
          ],
        },
      ],
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
