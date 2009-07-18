/*******************************************************************************

                          The CellCognition Project
                   Copyright (c) 2006 - 2009 Michael Held
                    Gerlich Lab, ETH Zurich, Switzerland

            CellCognition is distributed under the LGPL license.
                      See the LICENSE.txt for details.
               See trunk/AUTHORS.txt for author contributions.

*******************************************************************************/

// Author(s): Michael Held
// $Date$
// $Rev$
// $URL: https://svn.cellcognition.org/mito/trunk/include/mito/reader/wrap_lsm#$

#include <boost/python.hpp>

#include "vigra/stdimage.hxx"
#include "vigra/basicimage.hxx"
#include "vigra/basicimageview.hxx"
#include "pyvigra/converters.hxx"

#include "cecog/python/cecog.hxx"

using namespace boost::python;

// forward declarations:
void wrap_renderer();
//void wrap_lsmreader();

namespace cecog {
  namespace python {

    void wrap_cecog()
    {

      vigra::python::PySequenceToArrayVector< vigra::RGBValue<vigra::UInt8> >();
      wrap_renderer();
      //wrap_lsmreader();

    }

  } // namespace python

} // namespace cecog
