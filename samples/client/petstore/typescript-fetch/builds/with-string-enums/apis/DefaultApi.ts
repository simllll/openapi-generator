/* tslint:disable */
/* eslint-disable */
/**
 * Enum test
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import * as runtime from '../runtime';
import {
    EnumPatternObject,
    EnumPatternObjectFromJSON,
    EnumPatternObjectToJSON,
    FakeEnumRequestInlineInlineObject,
    FakeEnumRequestInlineInlineObjectFromJSON,
    FakeEnumRequestInlineInlineObjectToJSON,
    FakeEnumRequestInlineInlineResponse200,
    FakeEnumRequestInlineInlineResponse200FromJSON,
    FakeEnumRequestInlineInlineResponse200ToJSON,
    NumberEnum,
    NumberEnumFromJSON,
    NumberEnumToJSON,
    StringEnum,
    StringEnumFromJSON,
    StringEnumToJSON,
} from '../models';

export interface FakeEnumRequestGetInlineRequest {
    stringEnum?: FakeEnumRequestGetInlineStringEnumEnum;
    nullableStringEnum?: string | null;
    numberEnum?: FakeEnumRequestGetInlineNumberEnumEnum;
    nullableNumberEnum?: number | null;
}

export interface FakeEnumRequestGetRefRequest {
    stringEnum?: StringEnum;
    nullableStringEnum?: StringEnum | null;
    numberEnum?: NumberEnum;
    nullableNumberEnum?: NumberEnum | null;
}

export interface FakeEnumRequestPostInlineRequest {
    fakeEnumRequestInlineInlineObject?: FakeEnumRequestInlineInlineObject;
}

export interface FakeEnumRequestPostRefRequest {
    enumPatternObject?: EnumPatternObject;
}

/**
 * 
 */
export class DefaultApi extends runtime.BaseAPI {

    /**
     */
    async fakeEnumRequestGetInlineRaw(requestParameters: FakeEnumRequestGetInlineRequest, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<runtime.ApiResponse<FakeEnumRequestInlineInlineResponse200>> {
        const queryParameters: any = {};

        if (requestParameters.stringEnum !== undefined) {
            queryParameters['string-enum'] = requestParameters.stringEnum;
        }

        if (requestParameters.nullableStringEnum !== undefined) {
            queryParameters['nullable-string-enum'] = requestParameters.nullableStringEnum;
        }

        if (requestParameters.numberEnum !== undefined) {
            queryParameters['number-enum'] = requestParameters.numberEnum;
        }

        if (requestParameters.nullableNumberEnum !== undefined) {
            queryParameters['nullable-number-enum'] = requestParameters.nullableNumberEnum;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/fake/enum-request-inline`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => FakeEnumRequestInlineInlineResponse200FromJSON(jsonValue));
    }

    /**
     */
    async fakeEnumRequestGetInline(requestParameters: FakeEnumRequestGetInlineRequest = {}, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<FakeEnumRequestInlineInlineResponse200> {
        const response = await this.fakeEnumRequestGetInlineRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async fakeEnumRequestGetRefRaw(requestParameters: FakeEnumRequestGetRefRequest, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<runtime.ApiResponse<EnumPatternObject>> {
        const queryParameters: any = {};

        if (requestParameters.stringEnum !== undefined) {
            queryParameters['string-enum'] = requestParameters.stringEnum;
        }

        if (requestParameters.nullableStringEnum !== undefined) {
            queryParameters['nullable-string-enum'] = requestParameters.nullableStringEnum;
        }

        if (requestParameters.numberEnum !== undefined) {
            queryParameters['number-enum'] = requestParameters.numberEnum;
        }

        if (requestParameters.nullableNumberEnum !== undefined) {
            queryParameters['nullable-number-enum'] = requestParameters.nullableNumberEnum;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        const response = await this.request({
            path: `/fake/enum-request-ref`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => EnumPatternObjectFromJSON(jsonValue));
    }

    /**
     */
    async fakeEnumRequestGetRef(requestParameters: FakeEnumRequestGetRefRequest = {}, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<EnumPatternObject> {
        const response = await this.fakeEnumRequestGetRefRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async fakeEnumRequestPostInlineRaw(requestParameters: FakeEnumRequestPostInlineRequest, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<runtime.ApiResponse<FakeEnumRequestInlineInlineObject>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/fake/enum-request-inline`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: FakeEnumRequestInlineInlineObjectToJSON(requestParameters.fakeEnumRequestInlineInlineObject),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => FakeEnumRequestInlineInlineObjectFromJSON(jsonValue));
    }

    /**
     */
    async fakeEnumRequestPostInline(requestParameters: FakeEnumRequestPostInlineRequest = {}, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<FakeEnumRequestInlineInlineObject> {
        const response = await this.fakeEnumRequestPostInlineRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     */
    async fakeEnumRequestPostRefRaw(requestParameters: FakeEnumRequestPostRefRequest, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<runtime.ApiResponse<EnumPatternObject>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        const response = await this.request({
            path: `/fake/enum-request-ref`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: EnumPatternObjectToJSON(requestParameters.enumPatternObject),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => EnumPatternObjectFromJSON(jsonValue));
    }

    /**
     */
    async fakeEnumRequestPostRef(requestParameters: FakeEnumRequestPostRefRequest = {}, initOverrides?: RequestInit | runtime.InitOverideFunction): Promise<EnumPatternObject> {
        const response = await this.fakeEnumRequestPostRefRaw(requestParameters, initOverrides);
        return await response.value();
    }

}

/**
  * @export
  * @enum {string}
  */
export enum FakeEnumRequestGetInlineStringEnumEnum {
    One = 'one',
    Two = 'two',
    Three = 'three'
}
/**
  * @export
  * @enum {string}
  */
export enum FakeEnumRequestGetInlineNumberEnumEnum {
    NUMBER_1 = 1,
    NUMBER_2 = 2,
    NUMBER_3 = 3
}
