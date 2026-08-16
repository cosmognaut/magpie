<script lang="ts">
	import Genre from './lib/Genre.svelte'
	import Search from './lib/Search.svelte'
	import { genreList } from './globals.svelte'

	let query: string = $state('');
	let found: string[] = $derived(genreList.filter((genre: string) => (genre.toLowerCase()).includes(query)));

	// see https://zhangpascal.medium.com/how-to-properly-type-event-handlers-in-svelte-with-typescript-8e098c756eb9 on how to type event handlers.
	function onInput(event: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		query = event.currentTarget.value.toLowerCase();
	}
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

<Search onInput={onInput}/>

<!-- when there's no input, found is still the entire genreList -->
{#if found.length !== 0}
	{#each found as genre}
		<Genre name={genre}/>
	{/each}
{:else}
	<div class="mt-4 mb-4 ml-4">
	 <p class="text-xl">Nothing found!</p>
	</div>
{/if}

<div class="mt-4 ml-4 mb-4 text-center">
 <p>A cosmognaut production.</p>
</div>
