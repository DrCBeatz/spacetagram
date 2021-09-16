<style>
  header {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    height: 4rem;
    background: #cf0056;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.26);
    z-index: 1000;
  }

  h1 {
    color: white;
    font-family: "Roboto Slab", serif;
    margin: 0;
    text-align: left;
  }
  .title {
    /* text-align: right; */
    /* margin-left: auto; */
    /* margin-left: 20px; */
    margin-left: 20px;
  }
  .search {
    margin-top: 5px;
    /* margin-left: 20px; */
        margin-left: auto;
    /* margin-left: 20px; */
    margin-right: 20px;

  }
</style>

<header>
  <h1 class="title"><slot name="title"></slot></h1>
  
  <div class="search"><slot name = search></slot></div>
    
</header>
