<!-- if Search can be a component, so can be header! -->
<script lang="ts">
	let { statistics } = $props();
</script>

<div class="flex gap-2 flex-col justify-center items-center">
	<h1 class="text-7xl text-center mt-10 font-display text-emerald-500 mb-2">magpie</h1>
	<p class="text-lg max-w-lg text-center font-mono font-normal leading-relaxed mx-auto">A curation of your own watch later videos, powered with genre classification to get you to watch whatever you want. Select a genre and start watching, or search for a genre using the search bar below.</p>
	<p class="mt-10 text-center text-2xl mb-20"><span class="text-emerald-500">{statistics[1] === 0 ? '?' : statistics[1]}</span> videos // <span class="text-emerald-500">{statistics[0][0] === '' ? '?' : statistics[0].length}</span> genres</p>
</div>
