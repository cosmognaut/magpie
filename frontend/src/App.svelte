<script>
	import Genre from './lib/Genre.svelte'
	import Search from './lib/Search.svelte'
</script>

<nav class="flex flex-row justify-center items-center p-0.5 gap-100 mt-5">	
	<p class="font-mono font-bold">[ WHY? ]</p>
	<p class="font-mono font-bold">[ HOME ]</p>
	<p class="font-mono font-bold">[ HOW? ]</p>
</nav>

<div class="flex gap-2 flex-col justify-center items-center">
	<h1 class="text-6xl text-center mt-5 font-display text-emerald-500">magpie</h1>
	<p class="text-lg max-w-lg text-center font-mono font-normal">A curation of your own watch later videos along with genre classification to get you to watch whatever you want.</p>
</div>

<Search/>

<Genre/>
<Genre/>
<Genre/>
<Genre/>
<Genre/>
<Genre/>
<Genre/>
<Genre/>
