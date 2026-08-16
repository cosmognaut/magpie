<script lang="ts">
	let { value=$bindable() } = $props();
</script>

<div class="mr-4 ml-4">
	<input type="text" placeholder="Search genres..." class="border p-4 mt-10 mb-2 px-4 focus:outline-none text-xl w-full focus:border-emerald-500"  bind:value={value}/>
</div>
