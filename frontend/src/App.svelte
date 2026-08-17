<script lang="ts">
	import Genre from './lib/Genre.svelte'
	import Search from './lib/Search.svelte'
	import { genreList } from './globals.svelte'

	let query: string = $state(''); // user query inside the search box
	let found: string[] = $derived(genreList.filter((genre: string) => (genre.toLowerCase()).includes(query))); // found genres
	let focusElement: Search; // the component instance we need access to
	let keyCombinationCanHappen: boolean = false; // for CTRL-K, see advancedSearch
	let keyCombinationActivated: boolean = false;

	function onInput(event: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		// convert the user's query in the search bar to lower case and assign it to state
		query = event.currentTarget.value.toLowerCase();
	}

	function advancedSearch(event: KeyboardEvent) {
		// this is for CTRL-K. Prevent the default behaviour which would be focusing on the browser-default search bar.
		// we call focus() on the focusElement, which is a reference to the Search component instance.

		// for debugging
		console.log(event.key);
		if (event.key === 'Control') keyCombinationCanHappen = true;
		if (keyCombinationCanHappen && event.key === 'k') {
			// console.log(keyCombinationCanHappen);
			keyCombinationActivated = true;
			event.preventDefault();
			focusElement.callFocus();
		}
		if (keyCombinationActivated) {
			// reset everything back to original values if key combination was activated to await future combinations
			keyCombinationCanHappen = false;
			keyCombinationActivated = false;
		}
	}

	// we need to interact with the world outside of Svelte's reactivity - the DOM
	// hence, we use an effect here
	$effect( () => {
		document.addEventListener('keydown', advancedSearch);

		return () => {
			removeEventListener('keydown', advancedSearch);
		}
	});

	// see https://zhangpascal.medium.com/how-to-properly-type-event-handlers-in-svelte-with-typescript-8e098c756eb9 on how to type event handlers.
</script>

<nav class="md:flex flex-row justify-center items-center p-0.5 gap-100 mt-5 text-center">	
	<p class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors">[ WHY? ]</p>
	<p class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors">[ HOME ]</p>
	<p class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors">[ HOW? ]</p>
</nav>

<div class="flex gap-2 flex-col justify-center items-center">
	<h1 class="text-6xl text-center mt-5 font-display text-emerald-500">magpie</h1>
	<p class="text-lg max-w-lg text-center font-mono font-normal">A curation of your own watch later videos along with genre classification to get you to watch whatever you want.</p>
</div>

<Search onInput={onInput} bind:this={focusElement}/>

<!-- when there's no input, found is still the entire genreList -->
{#if found.length !== 0}
	{#each found as genre}
		<Genre name={genre}/>
	{/each}
{:else}
	<div class="mt-12 mb-4 ml-4 w-100vw h-100vh">
	 <p class="text-4xl text-center font-light">We don't have that genre!</p>
	 <p class="text-xl text-center mt-2 font-extralight">Watch something else, maybe?</p>
	</div>
{/if}

<footer class="mt-10 ml-4 mb-4 text-center">
 <p>A cosmognaut production.</p>
</footer>
