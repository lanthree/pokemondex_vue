<template>
  <div id="app">
    <el-container>
      <el-aside style="width: 230px">
        <div class="search">
          <el-input
            autofocus="true"
            placeholder="输入关键字进行过滤"
            v-model="filterText"
          >
          </el-input>
        </div>
        <el-scrollbar id="pokedex" :style="{ height: slbHeight }">
          <el-tree
            class="filter-tree"
            :data="data"
            :props="defaultProps"
            default-expand-all
            :filter-node-method="filterNode"
            @node-click="clickNode"
            ref="tree"
            v-if="refreshed"
          >
          </el-tree>
        </el-scrollbar>
      </el-aside>
      <el-main id="content">
        <el-scrollbar :style="{ height: contentHeight }">
          <Content :bid="bid" v-if="selected" />
        </el-scrollbar>
      </el-main>
    </el-container>
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
      clientHeight: "", //浏览器可视区域高度
      slbHeight: "",
      contentHeight: "",
      timer: false,
      refreshed: false,
    };
  },
  components: {
    Content,
  },
  methods: {
    filterNode(value, data) {
      this.clearBig();

      if (!value) return true;
      if (data.match === undefined) return false;
      if (data.match.indexOf(value) === -1) return false;

      this.changeBid(data.bid);
      return true;
    },
    clickNode(data) {
      this.clearBig();
      this.changeBid(data.bid);
    },
    changeBid(bid) {
      console.log(bid, this.bid, this.selected);
      if (bid === undefined) return;
      if (this.bid !== "") return;

      this.selected = false;
      this.bid = bid;
      this.$nextTick(() => {
        console.log("rendering ", this.bid);
        this.selected = true;
      });
    },
    clearBig() {
      if (this.selected === true) this.bid = "";
    },
    changeFixed(clientHeight) {
      console.log(clientHeight);
      this.slbHeight = clientHeight - 70 + "px";
      this.contentHeight = clientHeight - 10 + "px";
      this.refreshed = true;
    },
  },
  mounted() {
    const that = this;
    this.changeFixed(`${document.documentElement.clientHeight}`);

    window.onresize = () => {
      return (() => {
        that.clientHeight = `${document.documentElement.clientHeight}`;
      })();
    };
  },
  watch: {
    filterText(val) {
      this.$refs.tree.filter(val);
    },
    clientHeight(val) {
      if (!this.timer) {
        //如果clientHeight 发生改变，这个函数就会运行
        this.changeFixed(val);
        this.timer = true;
        let _this = this;
        setTimeout(function () {
          _this.timer = false;
        }, 100);
      }
    },
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: white;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0px;
  height: 100%;
}
.filter-tree {
  margin-top: 20px;
}
.el-aside {
  margin: 10px;
}
#pokedex {
  margin-top: 10px;
}
.search {
  margin-left: 10px;
  margin-right: 10px;
}
#content {
  padding: 0;
  margin-top: 5px;
  margin-bottom: 5px;
  margin-right: 10px;
}
</style>
