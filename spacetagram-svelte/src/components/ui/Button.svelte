<script>
  export let type = "button";
  export let href = null;
  export let mode = null;
  export let color = null;
  export let disabled = false;
</script>

<style>
  button,
  a {
    font: inherit;
    border: 1px solid #485063;
    background: #485063;
    /* border: 1px solid #cf0056;
    background: #cf0056; */
    padding: 0.5rem 1rem;
    color: white;
    border-radius: 5px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.26);
    cursor: pointer;
    text-decoration: none;
  }

  button:focus {
    outline: none;
  }

  button:hover,
  button:active,
  a:hover,
  a:active {
    background: #343d52;
    border-color: #343d52;
    /* background: #e40763;
    border-color: #e40763; */
    opacity: 0.75;
    box-shadow: 1px 1px 8px rgba(77, 51, 51, 0.26);
  }

  button:disabled,
  button:disabled:hover,
  button:disabled:active {
    background: #ccc;
    border-color: #ccc;
    color: #959595;
    box-shadow: none;
    cursor: not-allowed;
  }

  .success {
    background: #01a129;
    border-color: #01a129;
    /* background: #01a129;
    border-color: #01a129; */
  }

  .success:hover,
  .success:active {
    background: #1ac745;
    border-color: #1ac745;
    /* background: #1ac745;
    border-color: #1ac745; */
  }

  .outline {
    background: white;
    color: #485063;
    /* color: #cf0056; */
    opacity: 1;
    box-shadow: none;
    
  }

  .outline:hover,
  .outline:active {
    /* background: #ffc7de; */
    background: rgb(218, 218, 218);
    /* background: #858b97; */
    box-shadow: none;
  }

  .outline:disabled,
  .outline:disabled:hover,
  .outline:disabled:active {
    background: transparent;
    color: #ccc;
  }

  .outline.success {
    border-color: #343d52;
    color: #343d52;
  }

  .outline.success:hover,
  .outline.success:active {
    background: rgb(218, 218, 218);
    opacity: 1;
  }

  .center-button {
    margin:0 auto;
    display:block;
}
</style>

{#if href}
  <a {href}>
    <slot />
  </a>
{:else}
  <button class="{mode} {color}" {type} on:click {disabled}>
    <slot />
  </button>
{/if}
