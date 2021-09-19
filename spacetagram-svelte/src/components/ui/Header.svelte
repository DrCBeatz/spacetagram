<style>
  header {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    height: 4rem;
    background: #485063;
    /* background: #858b97; */
    /* background: #717786; */
    opacity: 0.89;
    display: flex;
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
    margin-left: 20px;
  }

  .search {
    margin-top: 8px;
    margin-left: auto;
    margin-right: 20px;
  }

</style>

<header>
  <h1 class="title"><slot name="title"></slot></h1>
  
  <div class="search"><slot name = search></slot></div>
    
</header>
