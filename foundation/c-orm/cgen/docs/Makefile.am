
if HAVE_DOXYGEN

doxyfile.stamp:
	$(DOXYGEN) Doxyfile
	echo Timestamp > doxyfile.stamp

CLEANFILES = doxyfile.stamp

html-local: doxyfile.stamp

clean-local:
	rm -rf $(top_srcdir)/docs/html

endif
