<script lang="ts">
	let { onInput } = $props();
	let element: HTMLElement; // we have a reference to this element, as we've used bind:this on the input element below, to get a readonly binding on the DOM node

	export function callFocus(): void {
		// we export this function because we want the parent to respect the child's privacy, and want this to be accessible from App.svelte
		// the parent will have a reference to the component instance and can call callFocus on it such that the input element is in focus
		// to call .focus() on the input element itself, we need a reference to that element, which we get via bind:this on element
		element.focus();
	}
</script>

<div class="mr-4 ml-4">
	<input type="text" placeholder="Search genres... or CTRL-K" class="border p-4 mt-10 mb-2 px-4 focus:outline-none text-xl w-full focus:border-emerald-500 hover:border-emerald-500 transition-colors" oninput={onInput} bind:this={element}/>
</div>
