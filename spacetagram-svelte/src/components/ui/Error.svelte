<script>
    import Modal from './Modal.svelte';

    export let message;
</script>

<Modal title="An error occurred!" on:cancel>
    <p class="center-text">{message}</p>
</Modal>