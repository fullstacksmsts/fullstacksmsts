import React from 'react';
import { Link } from 'react-router-dom';

const NotFoundPage = () => {
  return (
    <div className="flex flex-col items-center justify-center py-16 px-4 text-center">
      <div className="bg-[var(--primary-blue)] text-white p-6 rounded-full inline-flex items-center justify-center w-24 h-24 mb-8">
        <span className="text-5xl font-bold">404</span>
      </div>
      
      <h1 className="text-3xl md:text-4xl font-bold text-[var(--primary-blue)] mb-4">
        Page Not Found
      </h1>
      
      <p className="text-lg text-gray-600 max-w-md mb-8">
        The page you are looking for might have been removed, had its name changed, 
        or is temporarily unavailable.
      </p>
      
      <div className="flex flex-col sm:flex-row gap-4">
        <Link 
          to="/" 
          className="bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white font-medium py-3 px-6 rounded-lg text-center transition duration-150"
        >
          Go to Homepage
        </Link>
        
        <Link 
          to="/courses" 
          className="bg-transparent hover:bg-[var(--primary-blue)] text-[var(--primary-blue)] hover:text-white border border-[var(--primary-blue)] font-medium py-3 px-6 rounded-lg text-center transition duration-150"
        >
          View SMSTS Courses
        </Link>
      </div>
      
      <div className="mt-16 bg-gray-50 p-8 rounded-lg max-w-2xl">
        <h2 className="text-xl font-bold text-[var(--primary-blue)] mb-4">
          Looking for SMSTS Training?
        </h2>
        
        <p className="text-gray-600 mb-6">
          FullStack SMSTS offers CITB-accredited SMSTS courses with a 98% pass rate. 
          Choose from weekend, weekday, and online options at just £360+VAT.
        </p>
        
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <Link 
            to="/blog" 
            className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center justify-center"
          >
            Read our Blog
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          </Link>
          
          <Link 
            to="/contact" 
            className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center justify-center"
          >
            Contact Us
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default NotFoundPage;
