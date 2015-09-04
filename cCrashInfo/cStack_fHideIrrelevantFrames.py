# "*" is applied to all exceptions.
# Exception codes and exception type ids can be used
# Frame addresses and simplified addresses can be used
from NTSTATUS import *;

dasIrrelevantTopFrameFunctions_xExceptionCodeOrTypeId = {
  "*": [
    "KERNELBASE.dll!RaiseException",
    "ntdll.dll!KiUserExceptionDispatch",
    "ntdll.dll!NtRaiseException",
    "ntdll.dll!RtlDispatchException",
    "ntdll.dll!RtlpExecuteHandlerForException",
    "ntdll.dll!ZwRaiseException",
  ],
  STATUS_ACCESS_VIOLATION: [
    "chrome_child.dll!memcpy",
  ],
  "AVE:NULL": [
    "0x0",
  ],
  STATUS_FAIL_FAST_EXCEPTION: [
    "EDGEHTML.dll!Abandonment::InduceAbandonment",
  ],
  STATUS_STACK_BUFFER_OVERRUN: [
    "ntdll.dll!KiUserExceptionDispatcher",
    "ntdll.dll!LdrpValidateUserCallTarget",
    "ntdll.dll!LdrpValidateUserCallTargetBitMapCheck",
    "ntdll.dll!LdrpValidateUserCallTargetBitMapRet",
    "ntdll.dll!LdrpValidateUserCallTargetEH",
    "ntdll.dll!RtlFailFast2",
    "ntdll.dll!RtlpHandleInvalidUserCallTarget",
  ],
  CPP_EXCEPTION_CODE: [
    "KERNELBASE.dll!RaiseException",
    "msvcrt.dll!CxxThrowException",
    "msvcrt.dll!_CxxThrowException",
    "MSVCR110.dll!CxxThrowException",
    "MSVCR110.dll!_CxxThrowException",
  ],
  STATUS_BREAKPOINT: [
    "kernel32.dll!DebugBreak",
    "ntdll.dll!DbgBreakPoint",
    "EDGEHTML.dll!Abandonment::InduceAbandonment",
  ],
  "HeapCorrupt": [
    "chrome_child.dll!_aligned_free",
    "chrome_child.dll!`anonymous namespace'::win_heap_free",
    "kernel32.dll!HeapFree",
    "ntdll.dll!RtlDebugFreeHeap",
    "ntdll.dll!RtlFreeHeap",
    "ntdll.dll!RtlpFreeHeap",
    "verifier.dll!AVrfDebugPageHeapFree",
    "verifier.dll!AVrfpDphCheckPageHeapBlock",
    "verifier.dll!AVrfpDphFindBusyMemory",
    "verifier.dll!AVrfpDphFindBusyMemoryAndRemoveFromBusyList",
  ],
  "OOM": [
    "chrome.dll!`anonymous namespace'::call_new_handler",
    "chrome.dll!`anonymous namespace'::generic_cpp_alloc",
    "chrome.dll!malloc",
    "chrome.dll!operator new",
    "chrome.dll!operator new[]",
    "chrome.dll!realloc",
    "chrome.dll!std::_Allocate",
    "chrome.dll!std::_Allocate<...>",
    "chrome.dll!std::allocator<...>::allocate",
    "chrome.dll!std::allocator<...>::allocate",
    "chrome.dll!std::basic_string<...>::append",
    "chrome.dll!std::basic_string<...>::assign",
    "chrome.dll!std::basic_string<...>::_Copy",
    "chrome.dll!std::basic_string<...>::{ctor}",
    "chrome.dll!std::basic_string<...>::_Grow",
    "chrome.dll!std::deque<...>::emplace_back<>",
    "chrome.dll!std::deque<...>::_Growmap",
    "chrome.dll!std::deque<...>::insert",
    "chrome.dll!std::deque<...>::push_back",
    "chrome.dll!std::deque<...>::resize",
    "chrome.dll!std::_Hash<...>::_Check_size",
    "chrome.dll!std::_Hash<...>::emplace",
    "chrome.dll!std::_Hash<...>::_Init",
    "chrome.dll!std::_Hash<...>::_Insert<...>",
    "chrome.dll!std::unordered_map<...>::operator[]",
    "chrome.dll!std::vector<...>::assign",
    "chrome.dll!std::vector<...>::_Buy",
    "chrome.dll!std::vector<...>::insert",
    "chrome.dll!std::vector<...>::_Insert_n",
    "chrome.dll!std::vector<...>::_Reallocate",
    "chrome.dll!std::_Wrap_alloc<...>::allocate",
    "chrome_child.dll!blink::DOMArrayBuffer::create",
    "chrome_child.dll!blink::DOMTypedArray<...>::create",
    "chrome_child.dll!blink::PurgeableVector::append",
    "chrome_child.dll!blink::PurgeableVector::reservePurgeableCapacity",
    "chrome_child.dll!blink::RawResource::appendData",
    "chrome_child.dll!blink::Resource::appendData",
    "chrome_child.dll!blink::SharedBuffer::append",
    "chrome_child.dll!blink::SharedBuffer::SharedBuffer",
    "chrome_child.dll!blink::ContiguousContainer<...>::allocateAndConstruct",
    "chrome_child.dll!blink::ContiguousContainer<...>::allocateAndConstruct<...>",
    "chrome_child.dll!blink::ContiguousContainer<...>::appendByMoving",
    "chrome_child.dll!blink::ContiguousContainer<...>::{ctor}",
    "chrome_child.dll!blink::ContiguousContainerBase::allocate",
    "chrome_child.dll!blink::ContiguousContainerBase::allocateNewBufferForNextAllocation",
    "chrome_child.dll!blink::ContiguousContainerBase::Buffer::Buffer",
    "chrome_child.dll!blink::ContiguousContainerBase::ContiguousContainerBase",
    "chrome_child.dll!v8::internal::Factory::NewRawOneByteString",
    "chrome_child.dll!v8::internal::Factory::NewRawTwoByteString",
    "chrome_child.dll!v8::internal::Factory::NewUninitializedFixedArray",
    "chrome_child.dll!v8::internal::Heap::AllocateRawFixedArray",
    "chrome_child.dll!v8::internal::Heap::AllocateUninitializedFixedArray",
    "chrome_child.dll!v8::internal::Heap::FatalProcessOutOfMemory",
    "chrome_child.dll!WTF::ArrayBuffer::create",
    "chrome_child.dll!WTF::DefaultAllocator::allocateBacking",
    "chrome_child.dll!WTF::DefaultAllocator::allocateExpandedVectorBacking",
    "chrome_child.dll!WTF::DefaultAllocator::allocateVectorBacking",
    "chrome_child.dll!WTF::DefaultAllocator::allocateZeroedHashTableBacking<...>",
    "chrome_child.dll!WTF::fastMalloc",
    "chrome_child.dll!WTF::HashMap<...>::inlineAdd",
    "chrome_child.dll!WTF::HashTable<...>::add<...>",
    "chrome_child.dll!WTF::HashTable<...>::allocateTable",
    "chrome_child.dll!WTF::HashTable<...>::expand",
    "chrome_child.dll!WTF::HashTable<...>::rehash",
    "chrome_child.dll!WTF::partitionAlloc",
    "chrome_child.dll!WTF::partitionAllocGeneric",
    "chrome_child.dll!WTF::partitionAllocGenericFlags",
    "chrome_child.dll!WTF::partitionAllocSlowPath",
    "chrome_child.dll!WTF::partitionBucketAlloc",
    "chrome_child.dll!WTF::partitionOutOfMemory",
    "chrome_child.dll!WTF::partitionReallocGeneric",
    "chrome_child.dll!WTF::Partitions::bufferMalloc",
    "chrome_child.dll!WTF::Partitions::bufferRealloc",
    "chrome_child.dll!WTF::RefCounted<...>::operator new",
    "chrome_child.dll!WTF::String::utf8",
    "chrome_child.dll!WTF::StringBuilder::append",
    "chrome_child.dll!WTF::StringBuilder::appendUninitialized",
    "chrome_child.dll!WTF::StringBuilder::appendUninitializedSlow<...>",
    "chrome_child.dll!WTF::StringBuilder::reallocateBuffer<...>",
    "chrome_child.dll!WTF::StringImpl::operator new",
    "chrome_child.dll!WTF::StringImpl::reallocate",
    "chrome_child.dll!WTF::TypedArrayBase<...>::create<...>",
    "chrome_child.dll!WTF::Uint8ClampedArray::create",
    "chrome_child.dll!WTF::Vector<...>::append",
    "chrome_child.dll!WTF::Vector<...>::appendSlowCase<...>",
    "chrome_child.dll!WTF::Vector<...>::expandCapacity",
    "chrome_child.dll!WTF::Vector<...>::extendCapacity",
    "chrome_child.dll!WTF::Vector<...>::reserveCapacity",
    "chrome_child.dll!WTF::Vector<...>::reserveInitialCapacity ",
    "chrome_child.dll!WTF::Vector<...>::resize",
    "chrome_child.dll!WTF::Vector<...>::Vector<...>",
    "chrome_child.dll!WTF::VectorBuffer<...>::VectorBuffer<...>",
    "chrome_child.dll!WTF::VectorBuffer<...>::allocateExpandedBuffer",
    "chrome_child.dll!WTF::VectorBufferBase<...>::allocateBuffer",
    "chrome_child.dll!WTF::VectorBufferBase<...>::allocateExpandedBuffer",
    "EDGEHTML.dll!Abandonment::OutOfMemory",
    "EDGEHTML.dll!CAttrArray::Set",
    "EDGEHTML.dll!CBuffer::GrowBuffer",
    "EDGEHTML.dll!CHtPvPvBaseT<...>::Grow",
    "EDGEHTML.dll!CImplAry::AppendIndirect<36>",
    "EDGEHTML.dll!CImplAry::EnsureSize",
    "EDGEHTML.dll!CImplAry::EnsureSizeWorker",
    "EDGEHTML.dll!CImplAry::InitSize",
    "EDGEHTML.dll!CModernArray<...>::EnsureLargerCapacity",
    "EDGEHTML.dll!CStr::_Alloc",
    "EDGEHTML.dll!CStr::Set",
    "EDGEHTML.dll!_HeapRealloc<1>",
    "EDGEHTML.dll!Ptls6::TsAllocMemoryCore",
    "jscript9.dll!JavascriptDispatch_OOM_fatal_error",
    "jscript9.dll!Js::Exception::RaiseIfScriptActive",
    "mozglue.dll!arena_malloc_large",
    "mozglue.dll!arena_run_split",
    "mozglue.dll!je_malloc",
    "mozglue.dll!moz_xcalloc",
    "mozglue.dll!moz_xmalloc",
    "mozglue.dll!moz_xrealloc",
    "mozglue.dll!mozalloc_abort",
    "mozglue.dll!mozalloc_handle_oom",
    "xul.dll!js::CrashAtUnhandlableOOM",
    "xul.dll!js::MallocProvider<...>",
    "xul.dll!mozilla::CircularByteBuffer::SetCapacity",
    "xul.dll!NS_ABORT_OOM",
    "xul.dll!nsAString_internal::nsAString_internal",
    "xul.dll!nsACString_internal::AppendFunc",
    "xul.dll!nsBaseHashtable<...>::Put",
    "xul.dll!nsBaseHashtable::Put",
    "xul.dll!nsGlobalWindow::ClearDocumentDependentSlots",
    "xul.dll!nsPresArena::Allocate",
    "xul.dll!nsTArray_base<...>::EnsureCapacity",
    "xul.dll!nsTArray_Impl<...>::AppendElements",
    "xul.dll!nsTArray_Impl<...>::AppendElement<...>",
    "xul.dll!StatsCompartmentCallback",
    "xul.dll!std::_Allocate<char>",
    "xul.dll!std::basic_string<...>::_Copy",
    "xul.dll!std::basic_string<...>::assign",
    "xul.dll!std::vector<...>::_Reallocate",
    "xul.dll!std::vector<...>::_Reserve",
  ],
};

def cStack_fHideIrrelevantFrames(oStack, sExceptionTypeId, uExceptionCode):
  asIrrelevantTopFrameFunctions = (
    dasIrrelevantTopFrameFunctions_xExceptionCodeOrTypeId.get("*", []) +
    dasIrrelevantTopFrameFunctions_xExceptionCodeOrTypeId.get(sExceptionTypeId, []) +
    dasIrrelevantTopFrameFunctions_xExceptionCodeOrTypeId.get(uExceptionCode, [])
  );
  # For each frame
  for oFrame in oStack.aoFrames:
    # if it's not marked as irrelevant yet:
    if not oFrame.bIsHidden:
      # go through all irrelevant top frame functions:
      for sIrrelevantTopFrameFunction in asIrrelevantTopFrameFunctions:
        # and see if one of them is a match:
        if sIrrelevantTopFrameFunction in (oFrame.sAddress, oFrame.sSimplifiedAddress):
          oFrame.bIsHidden = True;
          # yes!, go to the next frame
          break;
      else:
        # no match found: this is not irrelevant
        return;