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
            <div
              class="custom-tree-node"
              slot-scope="{ node }"
              style="display: flex"
            >
              <img
                v-if="node.data.bid"
                v-bind:src="require('./assets/icons/' + node.data.bid + '.png')"
                style="height: 24px; flex: 0.3"
              />
              <span style="flex: 0.7">
                {{ node.label }}
              </span>
            </div>
          </el-tree>
        </el-scrollbar>
      </el-aside>
      <el-main id="content">
        <el-scrollbar :style="{ height: contentHeight }">
          <Content :bid="bid" :label="selected_label" v-if="selected" />
        </el-scrollbar>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Content from "./components/Content.vue";

export default {
  name: "App",
  data() {
    const { data } = require("./assets/data/indexes.js")
    return {
      bid: "001",
      selected_label: "001 妙蛙種子",

      selected: true,
      //
      filterText: "",
      data: data,
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
      if (bid === undefined) return;
      if (this.bid !== "") return;

      this.selected = false;
      this.bid = bid;
      this.$nextTick(() => {
        this.selected = true;
      });
    },
    clearBig() {
      if (this.selected === true) this.bid = "";
    },
    changeFixed(clientHeight) {
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
