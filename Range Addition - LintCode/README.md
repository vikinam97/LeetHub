# Range Addition

## Easy
<div>
   <div data-h5="false" class="content-wrapper-32rgvmtTEZlJxhYe-SXar4">
      <div class="sub-title-3tQamyyYH5-VXCEHKrzgsd with-action-3ISUSOCo8G5-PfWWWyKDb9">Description</div>
      <div class="react-markdown react-markdown-2P3YjvgELb5tvqGDu8Rkkt">
         <p>Assume you have an array of length <code>n</code> initialized with all <code>0</code>'s and are given <code>k</code> update operations.</p>
         <p>Each operation is represented as a triplet: <code>[startIndex, endIndex, inc]</code> which increments each element of subarray <code>A[startIndex ... endIndex]</code> (startIndex and endIndex inclusive) with <code>inc</code>.</p>
         <p>Return the modified array after all <code>k</code> operations were executed.</p>
      </div>
   </div>
   <div data-h5="false" class="content-wrapper-32rgvmtTEZlJxhYe-SXar4">
      <div class="sub-title-3tQamyyYH5-VXCEHKrzgsd">Example</div>
      <div class="react-markdown react-markdown-2P3YjvgELb5tvqGDu8Rkkt">
         <pre><div class="markdown-thumbnail-wrapper" style="height: auto; max-height: unset;"><pre style="display: block; overflow-x: auto; background: rgb(43, 43, 43); color: rgb(248, 248, 242); padding: 0.5em;"><code style="white-space: pre;"><span>Given:
</span><span>length = </span><span style="color: rgb(245, 171, 53);">5</span><span>,
</span>updates = 
[
<span>[</span><span style="color: rgb(245, 171, 53);">1</span><span>,  </span><span style="color: rgb(245, 171, 53);">3</span><span>,  </span><span style="color: rgb(245, 171, 53);">2</span><span>],
</span><span>[</span><span style="color: rgb(245, 171, 53);">2</span><span>,  </span><span style="color: rgb(245, 171, 53);">4</span><span>,  </span><span style="color: rgb(245, 171, 53);">3</span><span>],
</span><span>[</span><span style="color: rgb(245, 171, 53);">0</span><span>,  </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">-2</span><span>]
</span>]
<span>return [</span><span style="color: rgb(245, 171, 53);">-2</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span>, </span><span style="color: rgb(245, 171, 53);">5</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span>]
</span>
Explanation:
Initial state:
<span>[ </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span> ]
</span><span>After applying operation [</span><span style="color: rgb(245, 171, 53);">1</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>]:
</span><span>[ </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span> ]
</span><span>After applying operation [</span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">4</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span>]:
</span><span>[ </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">5</span><span>, </span><span style="color: rgb(245, 171, 53);">5</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span> ]
</span><span>After applying operation [</span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">2</span><span>, </span><span style="color: rgb(245, 171, 53);">-2</span><span>]:
</span><span>[</span><span style="color: rgb(245, 171, 53);">-2</span><span>, </span><span style="color: rgb(245, 171, 53);">0</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span>, </span><span style="color: rgb(245, 171, 53);">5</span><span>, </span><span style="color: rgb(245, 171, 53);">3</span><span> ]</span></code></pre></div></pre>
      </div>
   </div>
</div>