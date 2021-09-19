<script>
  export let src
  export let alt

  import { onMount } from 'svelte'

  let loaded = false
  let thisImage

  onMount(() => {
    thisImage.onload = () => {
      loaded = true
    }
  }) 

</script>

<style>

  img { 
display: block;
  margin-left: auto;
  margin-right: auto;
  min-height:200px;
  opacity: 0;
  transition: opacity 1200ms ease-out;
}

  img.loaded {
    opacity: 1;
  }

  .responsive-img {
  max-width: 100%;
  height: auto;
}
</style>

<img  class="responsive-img" {src} {alt} class:loaded bind:this={thisImage} loading="lazy" />